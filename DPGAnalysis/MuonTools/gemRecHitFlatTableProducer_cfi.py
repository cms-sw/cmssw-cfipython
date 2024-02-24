import FWCore.ParameterSet.Config as cms

gemRecHitFlatTableProducer = cms.EDProducer('GEMRecHitFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(
    allowAnyLabel_ = cms.required.PSetTemplate(
      expr = cms.required.string,
      doc = cms.required.string,
      type = cms.string('int')
    )
  ),
  detIdVariables = cms.PSet(
    allowAnyLabel_ = cms.required.PSetTemplate(
      expr = cms.required.string,
      doc = cms.required.string,
      type = cms.string('int')
    )
  ),
  globalPosVariables = cms.PSet(
    allowAnyLabel_ = cms.required.PSetTemplate(
      expr = cms.required.string,
      doc = cms.required.string
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
