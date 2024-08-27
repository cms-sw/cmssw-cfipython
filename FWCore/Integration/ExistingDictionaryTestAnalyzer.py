import FWCore.ParameterSet.Config as cms

def ExistingDictionaryTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExistingDictionaryTestAnalyzer',
    src = cms.InputTag('prod'),
    testVecUniqInt = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
