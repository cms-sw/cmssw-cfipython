import FWCore.ParameterSet.Config as cms

def SysShiftMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('SysShiftMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
