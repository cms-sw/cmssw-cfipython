import FWCore.ParameterSet.Config as cms

def ExistingDictionaryTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExistingDictionaryTestAnalyzer',
    src = cms.InputTag('prod'),
    testVecUniqInt = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
