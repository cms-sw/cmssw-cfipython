import FWCore.ParameterSet.Config as cms

def GaussEvtVtxGenerator(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
