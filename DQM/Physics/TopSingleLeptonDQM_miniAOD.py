import FWCore.ParameterSet.Config as cms

def TopSingleLeptonDQM_miniAOD(**kwargs):
  mod = cms.EDProducer('TopSingleLeptonDQM_miniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
