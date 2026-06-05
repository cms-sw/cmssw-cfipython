import FWCore.ParameterSet.Config as cms

def DSAMuonTableProducer(*args, **kwargs):
  mod = cms.EDProducer('DSAMuonTableProducer',
    name = cms.required.string,
    dsaMuons = cms.required.InputTag,
    muons = cms.required.InputTag,
    primaryVertex = cms.required.InputTag,
    beamspot = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
