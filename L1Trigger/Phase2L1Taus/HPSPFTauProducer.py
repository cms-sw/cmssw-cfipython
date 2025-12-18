import FWCore.ParameterSet.Config as cms

def HPSPFTauProducer(*args, **kwargs):
  mod = cms.EDProducer('HPSPFTauProducer',
    useJetSeeds = cms.bool(True),
    minPFTauPt = cms.double(20),
    minSignalConeSize = cms.double(0.05),
    isolationQualityCuts = cms.PSet(
      neutralHadron = cms.PSet(
        minPt = cms.double(0)
      ),
      muon = cms.PSet(
        maxDz = cms.double(0.4),
        minPt = cms.double(0)
      ),
      electron = cms.PSet(
        maxDz = cms.double(0.4),
        minPt = cms.double(0)
      ),
      photon = cms.PSet(
        minPt = cms.double(0)
      ),
      chargedHadron = cms.PSet(
        maxDz = cms.double(0.4),
        minPt = cms.double(0)
      )
    ),
    stripSizePhi = cms.double(0.2),
    minSeedJetPt = cms.double(30),
    maxChargedRelIso = cms.double(1),
    minSeedChargedPFCandPt = cms.double(5),
    srcL1PFCands = cms.InputTag('l1tLayer1', 'PF'),
    stripSizeEta = cms.double(0.05),
    maxLeadChargedPFCandEta = cms.double(2.4),
    deltaRCleaning = cms.double(0.4),
    useStrips = cms.bool(True),
    maxSeedChargedPFCandDz = cms.double(1000),
    minLeadChargedPFCandPt = cms.double(1),
    maxSeedChargedPFCandEta = cms.double(2.4),
    applyPreselection = cms.bool(False),
    isolationConeSize = cms.double(0.4),
    srcL1Vertices = cms.InputTag('l1tVertexFinderEmulator', 'L1VerticesEmulation'),
    maxChargedIso = cms.double(1000),
    signalQualityCuts = cms.PSet(
      neutralHadron = cms.PSet(
        minPt = cms.double(0)
      ),
      muon = cms.PSet(
        maxDz = cms.double(0.4),
        minPt = cms.double(0)
      ),
      electron = cms.PSet(
        maxDz = cms.double(0.4),
        minPt = cms.double(0)
      ),
      photon = cms.PSet(
        minPt = cms.double(0)
      ),
      chargedHadron = cms.PSet(
        maxDz = cms.double(0.4),
        minPt = cms.double(0)
      )
    ),
    useChargedPFCandSeeds = cms.bool(True),
    maxLeadChargedPFCandDz = cms.double(1000),
    maxSeedJetEta = cms.double(2.4),
    signalConeSize = cms.string('2.8/max(1., pt)'),
    srcL1Jets = cms.InputTag('l1tPhase1JetCalibrator9x9trimmed', 'Phase1L1TJetFromPfCandidates'),
    debug = cms.untracked.bool(False),
    maxPFTauEta = cms.double(2.4),
    maxSignalConeSize = cms.double(0.1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
