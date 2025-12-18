import FWCore.ParameterSet.Config as cms

def EcalTPGParamReaderFromDB(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTPGParamReaderFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
