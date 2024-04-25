import FWCore.ParameterSet.Config as cms

cscAlctDigiFlatTableProducer = cms.EDProducer('CSCAlctDigiFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(
    allowAnyLabel_ = cms.required.PSetTemplate(
      expr = cms.required.string,
      doc = cms.required.string,
      lazyEval = cms.untracked.bool(False),
      type = cms.string('int')
    )
  ),
  detIdVariables = cms.PSet(
    allowAnyLabel_ = cms.required.PSetTemplate(
      expr = cms.required.string,
      doc = cms.required.string,
      lazyEval = cms.required.untracked.bool,
      type = cms.string('int')
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
