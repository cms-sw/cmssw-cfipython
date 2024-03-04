import FWCore.ParameterSet.Config as cms

def DemoGlobalDQMEDAnalyzer(**kwargs):
  mod = cms.EDProducer('DemoGlobalDQMEDAnalyzer',
    folder = cms.string('MY_FOLDER'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
