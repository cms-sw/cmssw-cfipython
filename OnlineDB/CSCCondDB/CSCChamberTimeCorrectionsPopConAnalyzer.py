import FWCore.ParameterSet.Config as cms

def CSCChamberTimeCorrectionsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCChamberTimeCorrectionsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
