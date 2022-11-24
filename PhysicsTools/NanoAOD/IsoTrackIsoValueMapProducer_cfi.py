import FWCore.ParameterSet.Config as cms

IsoTrackIsoValueMapProducer = cms.EDProducer('IsoTrackIsoValueMapProducer',
  src = cms.required.InputTag,
  relative = cms.required.bool,
  doQuadratic = cms.bool(False),
  EAFile_MiniIso = cms.required.FileInPath,
  rho_MiniIso = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
