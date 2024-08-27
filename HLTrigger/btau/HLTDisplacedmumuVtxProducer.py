import FWCore.ParameterSet.Config as cms

def HLTDisplacedmumuVtxProducer(**kwargs):
  mod = cms.EDProducer('HLTDisplacedmumuVtxProducer',
    Src = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    matchToPrevious = cms.bool(True),
    MaxEta = cms.double(2.5),
    MinPt = cms.double(0),
    MinPtPair = cms.double(0),
    MinInvMass = cms.double(1),
    MaxInvMass = cms.double(20),
    ChargeOpt = cms.int32(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
