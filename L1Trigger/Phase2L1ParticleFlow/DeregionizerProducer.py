import FWCore.ParameterSet.Config as cms

def DeregionizerProducer(**kwargs):
  mod = cms.EDProducer('DeregionizerProducer',
    RegionalPuppiCands = cms.InputTag('l1tLayer1', 'PuppiRegional'),
    nPuppiFinalBuffer = cms.uint32(128),
    nPuppiPerClk = cms.uint32(6),
    nPuppiFirstBuffers = cms.uint32(12),
    nPuppiSecondBuffers = cms.uint32(32),
    nPuppiThirdBuffers = cms.uint32(64),
    nInputFramesPerBX = cms.uint32(9),
    linkConfigs = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
