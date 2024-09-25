import FWCore.ParameterSet.Config as cms

def CSCMakePTLUT(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCMakePTLUT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
