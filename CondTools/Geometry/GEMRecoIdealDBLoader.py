import FWCore.ParameterSet.Config as cms

def GEMRecoIdealDBLoader(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMRecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
