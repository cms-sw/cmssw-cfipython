import FWCore.ParameterSet.Config as cms

def HcalSignalGeneratorTest(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalSignalGeneratorTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
