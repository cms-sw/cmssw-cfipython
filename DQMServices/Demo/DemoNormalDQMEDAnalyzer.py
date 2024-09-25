import FWCore.ParameterSet.Config as cms

def DemoNormalDQMEDAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('DemoNormalDQMEDAnalyzer',
    folder = cms.string('MY_FOLDER'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
