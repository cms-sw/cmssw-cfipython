import FWCore.ParameterSet.Config as cms

def ElectronExtendedTableProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronExtendedTableProducer',
    rho = cms.required.InputTag,
    electrons = cms.required.InputTag,
    primaryVertex = cms.required.InputTag,
    jets = cms.required.InputTag,
    jetsFat = cms.required.InputTag,
    jetsSub = cms.required.InputTag,
    name = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
