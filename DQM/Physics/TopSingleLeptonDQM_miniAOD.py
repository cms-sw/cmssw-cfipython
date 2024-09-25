import FWCore.ParameterSet.Config as cms

def TopSingleLeptonDQM_miniAOD(*args, **kwargs):
  mod = cms.EDProducer('TopSingleLeptonDQM_miniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
