import FWCore.ParameterSet.Config as cms

def HLTDisplacedtktktkVtxProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTDisplacedtktktkVtxProducer',
    Src = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    MaxEtaTk = cms.double(2.5),
    MinPtResTk1 = cms.double(0),
    MinPtResTk2 = cms.double(0),
    MinPtThirdTk = cms.double(0),
    MinPtRes = cms.double(0),
    MinPtTri = cms.double(0),
    MinInvMassRes = cms.double(1),
    MaxInvMassRes = cms.double(20),
    MinInvMass = cms.double(1),
    MaxInvMass = cms.double(20),
    massParticleRes1 = cms.double(0.4937),
    massParticleRes2 = cms.double(0.4937),
    massParticle3 = cms.double(0.1396),
    ChargeOpt = cms.int32(-1),
    ResOpt = cms.int32(1),
    triggerTypeDaughters = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
