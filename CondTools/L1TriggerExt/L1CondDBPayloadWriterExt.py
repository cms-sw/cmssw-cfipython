import FWCore.ParameterSet.Config as cms

def L1CondDBPayloadWriterExt(*args, **kwargs):
  mod = cms.EDAnalyzer('L1CondDBPayloadWriterExt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
