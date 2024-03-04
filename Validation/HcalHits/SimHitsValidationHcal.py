import FWCore.ParameterSet.Config as cms

def SimHitsValidationHcal(**kwargs):
  mod = cms.EDProducer('SimHitsValidationHcal',
    ModuleLabel = cms.string('g4SimHits'),
    HitCollection = cms.string('HcalHits'),
    Verbose = cms.bool(False),
    TestNumber = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
