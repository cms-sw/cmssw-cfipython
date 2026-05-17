import FWCore.ParameterSet.Config as cms

def FlatEvtVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('FlatEvtVtxGenerator',
    MinZ = cms.double(0),
    MaxZ = cms.double(0.001),
    MinT = cms.double(0),
    MaxT = cms.double(0.001),
    src = cms.required.InputTag,
    UseCylindricalCoords = cms.bool(False),
    MinX = cms.double(0),
    MaxX = cms.double(0.001),
    MinY = cms.double(0),
    MaxY = cms.double(0.001),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
