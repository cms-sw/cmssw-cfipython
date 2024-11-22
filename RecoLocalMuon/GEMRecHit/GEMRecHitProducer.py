import FWCore.ParameterSet.Config as cms

def GEMRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('GEMRecHitProducer',
    recAlgoConfig = cms.PSet(),
    recAlgo = cms.string('GEMRecHitStandardAlgo'),
    gemDigiLabel = cms.InputTag('muonGEMDigis'),
    applyMasking = cms.bool(False),
    ge21Off = cms.bool(False),
    maskFile = cms.optional.FileInPath,
    deadFile = cms.optional.FileInPath,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
