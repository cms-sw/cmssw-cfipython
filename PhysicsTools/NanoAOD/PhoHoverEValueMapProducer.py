import FWCore.ParameterSet.Config as cms

def PhoHoverEValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('PhoHoverEValueMapProducer',
    src = cms.required.InputTag,
    relative = cms.required.bool,
    QuadraticEAFile_HoverE = cms.required.FileInPath,
    rho = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
