import FWCore.ParameterSet.Config as cms

def EleIsoValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('EleIsoValueMapProducer',
    src = cms.required.InputTag,
    relative = cms.required.bool,
    doQuadratic = cms.bool(False),
    EAFile_MiniIso = cms.required.FileInPath,
    rho_MiniIso = cms.required.InputTag,
    EAFile_PFIso = cms.required.FileInPath,
    rho_PFIso = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
