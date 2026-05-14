import FWCore.ParameterSet.Config as cms

def FlatEvtVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('FlatEvtVtxGenerator',
    MinX = cms.double(0),
    MaxX = cms.double(0.001),
    MinY = cms.double(0),
    MaxY = cms.double(0.001),
    MinZ = cms.double(0),
    MaxZ = cms.double(0.001),
    MinT = cms.double(0),
    MaxT = cms.double(0.001),
    FixedR = cms.bool(False),
    MinR = cms.double(0),
    MaxR = cms.double(0.001),
    MinPhi = cms.double(-3.14159265359),
    MaxPhi = cms.double(3.14159265359),
    src = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
