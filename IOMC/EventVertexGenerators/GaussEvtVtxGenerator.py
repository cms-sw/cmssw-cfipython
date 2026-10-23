import FWCore.ParameterSet.Config as cms

def GaussEvtVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('GaussEvtVtxGenerator',
    MeanX = cms.double(0),
    MeanY = cms.double(0),
    MeanZ = cms.double(0),
    SigmaX = cms.double(0),
    SigmaY = cms.double(0),
    SigmaZ = cms.double(0),
    TimeOffset = cms.double(0),
    src = cms.required.InputTag,
    readDB = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
