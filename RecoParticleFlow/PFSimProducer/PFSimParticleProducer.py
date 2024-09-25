import FWCore.ParameterSet.Config as cms

def PFSimParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('PFSimParticleProducer',
    fastSimProducer = cms.untracked.InputTag('fastSimProducer', 'EcalHitsEB'),
    MCTruthMatchingInfo = cms.untracked.bool(False),
    RecTracks = cms.InputTag('trackerDrivenElectronSeeds'),
    Fitter = cms.string('KFFittingSmoother'),
    ecalRecHitsEE = cms.InputTag('caloRecHits', 'EcalRecHitsEE'),
    ecalRecHitsEB = cms.InputTag('caloRecHits', 'EcalRecHitsEB'),
    process_RecTracks = cms.untracked.bool(False),
    ParticleFilter = cms.PSet(),
    TTRHBuilder = cms.string('WithTrackAngle'),
    process_Particles = cms.untracked.bool(True),
    Propagator = cms.string('PropagatorWithMaterial'),
    sim = cms.InputTag('g4SimHits'),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
