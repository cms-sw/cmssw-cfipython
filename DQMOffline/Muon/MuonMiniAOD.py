import FWCore.ParameterSet.Config as cms

def MuonMiniAOD(*args, **kwargs):
  mod = cms.EDProducer('MuonMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
