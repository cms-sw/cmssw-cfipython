import FWCore.ParameterSet.Config as cms

def TruthLogicalGraphProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthLogicalGraphProducer',
    src = cms.InputTag('truthGraphProducer'),
    simTracks = cms.InputTag('g4SimHits'),
    simVertices = cms.InputTag('g4SimHits'),
    genEventHepMC3 = cms.InputTag('generatorSmeared'),
    genEventHepMC = cms.InputTag('generatorSmeared'),
    verbosity = cms.untracked.uint32(0),
    mergeGenSimVertices = cms.bool(True),
    simHitCollections = cms.VInputTag(
      'g4SimHits:HGCHitsEE',
      'g4SimHits:HGCHitsHEfront',
      'g4SimHits:HGCHitsHEback',
      'g4SimHits:EcalHitsEB',
      'g4SimHits:HcalHits'
    ),
    trackerSimHitCollections = cms.VInputTag(
      'g4SimHits:TrackerHitsPixelBarrelLowTof',
      'g4SimHits:TrackerHitsPixelBarrelHighTof',
      'g4SimHits:TrackerHitsPixelEndcapLowTof',
      'g4SimHits:TrackerHitsPixelEndcapHighTof',
      'g4SimHits:TrackerHitsTIBLowTof',
      'g4SimHits:TrackerHitsTIBHighTof',
      'g4SimHits:TrackerHitsTIDLowTof',
      'g4SimHits:TrackerHitsTIDHighTof',
      'g4SimHits:TrackerHitsTOBLowTof',
      'g4SimHits:TrackerHitsTOBHighTof',
      'g4SimHits:TrackerHitsTECLowTof',
      'g4SimHits:TrackerHitsTECHighTof'
    ),
    muonSimHitCollections = cms.VInputTag(
      'g4SimHits:MuonDTHits',
      'g4SimHits:MuonCSCHits',
      'g4SimHits:MuonRPCHits',
      'g4SimHits:MuonGEMHits',
      'g4SimHits:MuonME0Hits'
    ),
    postProcessing = cms.PSet(
      collapseIntermediateGenParticles = cms.bool(True),
      dropHitlessSimSubgraphs = cms.bool(True),
      reconstructablePdgIds = cms.vint32(111),
      seedPdgIds = cms.vint32(),
      seedParentDepth = cms.uint32(0),
      seedHadronFlavors = cms.vint32(),
      keepStableSpectators = cms.bool(True),
      attachSelectionSources = cms.bool(True),
      keepProductionSiblings = cms.bool(False),
      signalOnly = cms.bool(False),
      keepBunchCrossings = cms.vint32(),
      decayPdgIdGroups = cms.VPSet(
        template = cms.PSetTemplate(
          pdgIds = cms.vint32()
        )
      ),
      ignoredPdgIds = cms.vint32(),
      ignoredParticleIds = cms.vuint32()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
