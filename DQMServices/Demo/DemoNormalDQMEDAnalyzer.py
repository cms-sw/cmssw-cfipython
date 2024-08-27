import FWCore.ParameterSet.Config as cms

def DemoNormalDQMEDAnalyzer(**kwargs):
  mod = cms.EDProducer('DemoNormalDQMEDAnalyzer',
    folder = cms.string('MY_FOLDER'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
