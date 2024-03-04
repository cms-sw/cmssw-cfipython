import FWCore.ParameterSet.Config as cms

def CSCMakePTLUT(**kwargs):
  mod = cms.EDAnalyzer('CSCMakePTLUT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
