import FWCore.ParameterSet.Config as cms

nanoAODDQM = cms.EDProducer('NanoAODDQM',
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
