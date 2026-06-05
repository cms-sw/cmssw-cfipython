import FWCore.ParameterSet.Config as cms

def MuonExtendedTableProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonExtendedTableProducer',
    rho = cms.required.InputTag,
    muons = cms.required.InputTag,
    primaryVertex = cms.required.InputTag,
    beamspot = cms.required.InputTag,
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
