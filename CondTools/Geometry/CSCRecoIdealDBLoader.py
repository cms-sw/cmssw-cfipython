import FWCore.ParameterSet.Config as cms

def CSCRecoIdealDBLoader(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCRecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
