import FWCore.ParameterSet.Config as cms

PATJetUpdater = cms.EDProducer('PATJetUpdater',
  jetSource = cms.InputTag('no default'),
  sort = cms.bool(True),
  addTagInfos = cms.bool(True),
  tagInfoSources = cms.VInputTag(),
  addJetCorrFactors = cms.bool(True),
  jetCorrFactorsSource = cms.VInputTag(),
  addBTagInfo = cms.bool(True),
  addDiscriminators = cms.bool(True),
  discriminatorSources = cms.VInputTag(),
  printWarning = cms.bool(True),
  userData = cms.PSet(
    userClasses = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userFloats = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userInts = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userCands = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userFunctions = cms.vstring(),
    userFunctionLabels = cms.vstring()
  )
)
