import FWCore.ParameterSet.Config as cms

def DeregionizerProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
