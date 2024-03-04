import FWCore.ParameterSet.Config as cms

def L1CondDBPayloadWriterExt(**kwargs):
  mod = cms.EDAnalyzer('L1CondDBPayloadWriterExt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
