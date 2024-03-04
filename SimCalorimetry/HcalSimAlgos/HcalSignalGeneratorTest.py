import FWCore.ParameterSet.Config as cms

def HcalSignalGeneratorTest(**kwargs):
  mod = cms.EDAnalyzer('HcalSignalGeneratorTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
