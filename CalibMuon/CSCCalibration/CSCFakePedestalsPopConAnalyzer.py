import FWCore.ParameterSet.Config as cms

def CSCFakePedestalsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCFakePedestalsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
