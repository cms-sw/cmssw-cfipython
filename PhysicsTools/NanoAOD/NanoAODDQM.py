import FWCore.ParameterSet.Config as cms

def NanoAODDQM(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod