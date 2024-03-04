import FWCore.ParameterSet.Config as cms

def IsoTrackIsoValueMapProducer(**kwargs):
  mod = cms.EDProducer('IsoTrackIsoValueMapProducer',
    src = cms.required.InputTag,
    relative = cms.required.bool,
    doQuadratic = cms.bool(False),
    EAFile_MiniIso = cms.required.FileInPath,
    rho_MiniIso = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
