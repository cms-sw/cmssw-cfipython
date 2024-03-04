import FWCore.ParameterSet.Config as cms

def L1CondDBIOVWriterExt(**kwargs):
  mod = cms.EDAnalyzer('L1CondDBIOVWriterExt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
