import FWCore.ParameterSet.Config as cms

hltDisplacedtktkVtxProducer = cms.EDProducer('HLTDisplacedtktkVtxProducer',
  Src = cms.InputTag('hltL3MuonCandidates'),
  PreviousCandTag = cms.InputTag(''),
  MaxEta = cms.double(2.5),
  MinPt = cms.double(0),
  MinPtPair = cms.double(0),
  MinInvMass = cms.double(1),
  MaxInvMass = cms.double(20),
  massParticle1 = cms.double(0.1396),
  massParticle2 = cms.double(0.4937),
  ChargeOpt = cms.int32(-1),
  triggerTypeDaughters = cms.int32(0)
)
