import FWCore.ParameterSet.Config as cms

def EgammaHLTExtraProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTExtraProducer',
    minPtToSaveHits = cms.double(0),
    saveHitsPlusPi = cms.bool(False),
    saveHitsPlusHalfPi = cms.bool(True),
    recHitCountThresholds = cms.vdouble(
      0,
      0.5,
      1,
      1.5,
      2
    ),
    egCands = cms.VPSet(
      cms.PSet(
        ecalCands = cms.InputTag('hltEgammaCandidates'),
        gsfTracks = cms.InputTag('hltEgammaGsfTracks'),
        label = cms.string(''),
        pixelSeeds = cms.InputTag('hltEgammaElectronPixelSeeds')
      ),
      template = cms.PSetTemplate(
        ecalCands = cms.InputTag(''),
        pixelSeeds = cms.InputTag(''),
        gsfTracks = cms.InputTag(''),
        label = cms.string('')
      )
    ),
    ecal = cms.VPSet(
      cms.PSet(
        label = cms.string('EcalRecHitsEB'),
        src = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB')
      ),
      cms.PSet(
        label = cms.string('EcalRecHitsEE'),
        src = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE')
      ),
      template = cms.PSetTemplate(
        src = cms.InputTag(''),
        label = cms.string('')
      )
    ),
    hcal = cms.VPSet(
      cms.PSet(
        label = cms.string(''),
        src = cms.InputTag('hltHbhereco')
      ),
      template = cms.PSetTemplate(
        src = cms.InputTag(''),
        label = cms.string('')
      )
    ),
    trks = cms.VPSet(
      cms.PSet(
        label = cms.string(''),
        src = cms.InputTag('generalTracks')
      ),
      template = cms.PSetTemplate(
        src = cms.InputTag(''),
        label = cms.string('')
      )
    ),
    pfClusIso = cms.VPSet(
      cms.PSet(
        label = cms.string('Ecal'),
        src = cms.InputTag('hltParticleFlowClusterECALL1Seeded')
      ),
      cms.PSet(
        label = cms.string('EcalUnseeded'),
        src = cms.InputTag('hltParticleFlowClusterECALUnseeded')
      ),
      cms.PSet(
        label = cms.string('Hcal'),
        src = cms.InputTag('hltParticleFlowClusterHCAL')
      ),
      template = cms.PSetTemplate(
        src = cms.InputTag(''),
        label = cms.string('')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
