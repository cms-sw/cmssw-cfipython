import FWCore.ParameterSet.Config as cms

def HLTDisplacedmumumuVtxProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
