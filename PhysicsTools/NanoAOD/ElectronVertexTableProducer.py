import FWCore.ParameterSet.Config as cms

def ElectronVertexTableProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronVertexTableProducer',
    electrons = cms.required.InputTag,
    beamspot = cms.required.InputTag,
    primaryVertex = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
