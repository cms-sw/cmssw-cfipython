import FWCore.ParameterSet.Config as cms

PATJetUpdater = cms.EDProducer('PATJetUpdater',
  jetSource = cms.InputTag('no default'),
  addTagInfos = cms.bool(True),
  tagInfoSources = cms.VInputTag(),
  addJetCorrFactors = cms.bool(True),
  jetCorrFactorsSource = cms.VInputTag(),
  addBTagInfo = cms.bool(True),
  addDiscriminators = cms.bool(True),
  discriminatorSources = cms.VInputTag(),
  userData = cms.PSet(
    userClasses = cms.PSet(),
    userFloats = cms.PSet(),
    userInts = cms.PSet(),
    userCands = cms.PSet(),
    userFunctions = cms.vstring(),
    userFunctionLabels = cms.vstring()
  )
)
