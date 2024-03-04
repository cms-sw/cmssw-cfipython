import FWCore.ParameterSet.Config as cms

def CSCRecoIdealDBLoader(**kwargs):
  mod = cms.EDAnalyzer('CSCRecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
