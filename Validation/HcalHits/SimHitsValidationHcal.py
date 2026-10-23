import FWCore.ParameterSet.Config as cms

def SimHitsValidationHcal(*args, **kwargs):
  mod = cms.EDProducer('SimHitsValidationHcal',
    ModuleLabel = cms.string('g4SimHits'),
    HitCollection = cms.string('HcalHits'),
    Verbose = cms.bool(False),
    TestNumber = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
