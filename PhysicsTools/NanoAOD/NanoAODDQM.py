import FWCore.ParameterSet.Config as cms

def NanoAODDQM(*args, **kwargs):
  mod = cms.EDProducer('NanoAODDQM',
    vplots = cms.PSet(
      allowAnyLabel_ = cms.required.PSetTemplate(
        sels = cms.PSet(
          allowAnyLabel_ = cms.required.string
        ),
        plots = cms.required.VPSet
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
