import FWCore.ParameterSet.Config as cms

def HLTDisplacedmumumuVtxProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTDisplacedmumumuVtxProducer',
    Src = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    MaxEta = cms.double(2.5),
    MinPt = cms.double(0),
    MinPtTriplet = cms.double(0),
    MinInvMass = cms.double(1),
    MaxInvMass = cms.double(20),
    ChargeOpt = cms.int32(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
